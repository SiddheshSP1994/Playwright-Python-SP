import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-4801", "title": "Checkout scenario 4801", "data": {"sku": "SKU4801", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4801@example.com", "threshold": 10}},
    {"id": "CHECKOUT-4802", "title": "Checkout scenario 4802", "data": {"sku": "SKU4802", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4802@example.com", "threshold": 20}},
    {"id": "CHECKOUT-4803", "title": "Checkout scenario 4803", "data": {"sku": "SKU4803", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4803@example.com", "threshold": 30}},
    {"id": "CHECKOUT-4804", "title": "Checkout scenario 4804", "data": {"sku": "SKU4804", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4804@example.com", "threshold": 40}},
    {"id": "CHECKOUT-4805", "title": "Checkout scenario 4805", "data": {"sku": "SKU4805", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4805@example.com", "threshold": 50}},
    {"id": "CHECKOUT-4806", "title": "Checkout scenario 4806", "data": {"sku": "SKU4806", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4806@example.com", "threshold": 60}},
    {"id": "CHECKOUT-4807", "title": "Checkout scenario 4807", "data": {"sku": "SKU4807", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4807@example.com", "threshold": 70}},
    {"id": "CHECKOUT-4808", "title": "Checkout scenario 4808", "data": {"sku": "SKU4808", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4808@example.com", "threshold": 80}},
    {"id": "CHECKOUT-4809", "title": "Checkout scenario 4809", "data": {"sku": "SKU4809", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4809@example.com", "threshold": 90}},
    {"id": "CHECKOUT-4810", "title": "Checkout scenario 4810", "data": {"sku": "SKU4810", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4810@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
