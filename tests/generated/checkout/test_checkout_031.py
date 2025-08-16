import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-1801", "title": "Checkout scenario 1801", "data": {"sku": "SKU1801", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1801@example.com", "threshold": 10}},
    {"id": "CHECKOUT-1802", "title": "Checkout scenario 1802", "data": {"sku": "SKU1802", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1802@example.com", "threshold": 20}},
    {"id": "CHECKOUT-1803", "title": "Checkout scenario 1803", "data": {"sku": "SKU1803", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1803@example.com", "threshold": 30}},
    {"id": "CHECKOUT-1804", "title": "Checkout scenario 1804", "data": {"sku": "SKU1804", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1804@example.com", "threshold": 40}},
    {"id": "CHECKOUT-1805", "title": "Checkout scenario 1805", "data": {"sku": "SKU1805", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1805@example.com", "threshold": 50}},
    {"id": "CHECKOUT-1806", "title": "Checkout scenario 1806", "data": {"sku": "SKU1806", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1806@example.com", "threshold": 60}},
    {"id": "CHECKOUT-1807", "title": "Checkout scenario 1807", "data": {"sku": "SKU1807", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1807@example.com", "threshold": 70}},
    {"id": "CHECKOUT-1808", "title": "Checkout scenario 1808", "data": {"sku": "SKU1808", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1808@example.com", "threshold": 80}},
    {"id": "CHECKOUT-1809", "title": "Checkout scenario 1809", "data": {"sku": "SKU1809", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1809@example.com", "threshold": 90}},
    {"id": "CHECKOUT-1810", "title": "Checkout scenario 1810", "data": {"sku": "SKU1810", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1810@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
