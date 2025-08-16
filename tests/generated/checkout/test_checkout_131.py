import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-7801", "title": "Checkout scenario 7801", "data": {"sku": "SKU7801", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7801@example.com", "threshold": 10}},
    {"id": "CHECKOUT-7802", "title": "Checkout scenario 7802", "data": {"sku": "SKU7802", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7802@example.com", "threshold": 20}},
    {"id": "CHECKOUT-7803", "title": "Checkout scenario 7803", "data": {"sku": "SKU7803", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7803@example.com", "threshold": 30}},
    {"id": "CHECKOUT-7804", "title": "Checkout scenario 7804", "data": {"sku": "SKU7804", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7804@example.com", "threshold": 40}},
    {"id": "CHECKOUT-7805", "title": "Checkout scenario 7805", "data": {"sku": "SKU7805", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7805@example.com", "threshold": 50}},
    {"id": "CHECKOUT-7806", "title": "Checkout scenario 7806", "data": {"sku": "SKU7806", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7806@example.com", "threshold": 60}},
    {"id": "CHECKOUT-7807", "title": "Checkout scenario 7807", "data": {"sku": "SKU7807", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7807@example.com", "threshold": 70}},
    {"id": "CHECKOUT-7808", "title": "Checkout scenario 7808", "data": {"sku": "SKU7808", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7808@example.com", "threshold": 80}},
    {"id": "CHECKOUT-7809", "title": "Checkout scenario 7809", "data": {"sku": "SKU7809", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7809@example.com", "threshold": 90}},
    {"id": "CHECKOUT-7810", "title": "Checkout scenario 7810", "data": {"sku": "SKU7810", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7810@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
