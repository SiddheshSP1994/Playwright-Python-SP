import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-9961", "title": "Checkout scenario 9961", "data": {"sku": "SKU9961", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9961@example.com", "threshold": 610}},
    {"id": "CHECKOUT-9962", "title": "Checkout scenario 9962", "data": {"sku": "SKU9962", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9962@example.com", "threshold": 620}},
    {"id": "CHECKOUT-9963", "title": "Checkout scenario 9963", "data": {"sku": "SKU9963", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9963@example.com", "threshold": 630}},
    {"id": "CHECKOUT-9964", "title": "Checkout scenario 9964", "data": {"sku": "SKU9964", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9964@example.com", "threshold": 640}},
    {"id": "CHECKOUT-9965", "title": "Checkout scenario 9965", "data": {"sku": "SKU9965", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9965@example.com", "threshold": 650}},
    {"id": "CHECKOUT-9966", "title": "Checkout scenario 9966", "data": {"sku": "SKU9966", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9966@example.com", "threshold": 660}},
    {"id": "CHECKOUT-9967", "title": "Checkout scenario 9967", "data": {"sku": "SKU9967", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9967@example.com", "threshold": 670}},
    {"id": "CHECKOUT-9968", "title": "Checkout scenario 9968", "data": {"sku": "SKU9968", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9968@example.com", "threshold": 680}},
    {"id": "CHECKOUT-9969", "title": "Checkout scenario 9969", "data": {"sku": "SKU9969", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9969@example.com", "threshold": 690}},
    {"id": "CHECKOUT-9970", "title": "Checkout scenario 9970", "data": {"sku": "SKU9970", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9970@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
