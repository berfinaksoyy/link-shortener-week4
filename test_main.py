from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_shorten_and_redirect():
    r = client.post("/shorten", json={"url": "https://example.com"})
    assert r.status_code == 200
    code = r.json()["code"]
    assert code
    r2 = client.get(f"/{code}", follow_redirects=False)
    assert r2.status_code == 307
    assert r2.headers["location"] == "https://example.com"


def test_rejects_bad_url():
    r = client.post("/shorten", json={"url": "ftp://nope"})
    assert r.status_code == 400


def test_unknown_code_404():
    r = client.get("/does-not-exist", follow_redirects=False)
    assert r.status_code == 404


def test_click_counter_initial_zero():
    r = client.post("/shorten", json={"url": "https://example.com"})
    assert r.status_code == 200
    code = r.json()["code"]
    stats_resp = client.get(f"/stats/{code}")
    assert stats_resp.status_code == 200
    data = stats_resp.json()
    assert data["url"] == "https://example.com"
    assert data["clicks"] == 0


def test_click_counter_increments_on_redirect():
    r = client.post("/shorten", json={"url": "https://example.com/visited"})
    assert r.status_code == 200
    code = r.json()["code"]

    client.get(f"/{code}", follow_redirects=False)
    client.get(f"/{code}", follow_redirects=False)

    stats_resp = client.get(f"/stats/{code}")
    assert stats_resp.status_code == 200
    data = stats_resp.json()
    assert data["url"] == "https://example.com/visited"
    assert data["clicks"] == 2


def test_click_counter_unknown_code_404():
    r = client.get("/stats/does-not-exist")
    assert r.status_code == 404

