import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-3961", "title": "Checkout scenario 3961", "data": {"sku": "SKU3961", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3961@example.com", "threshold": 610}},
    {"id": "CHECKOUT-3962", "title": "Checkout scenario 3962", "data": {"sku": "SKU3962", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3962@example.com", "threshold": 620}},
    {"id": "CHECKOUT-3963", "title": "Checkout scenario 3963", "data": {"sku": "SKU3963", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3963@example.com", "threshold": 630}},
    {"id": "CHECKOUT-3964", "title": "Checkout scenario 3964", "data": {"sku": "SKU3964", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3964@example.com", "threshold": 640}},
    {"id": "CHECKOUT-3965", "title": "Checkout scenario 3965", "data": {"sku": "SKU3965", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3965@example.com", "threshold": 650}},
    {"id": "CHECKOUT-3966", "title": "Checkout scenario 3966", "data": {"sku": "SKU3966", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3966@example.com", "threshold": 660}},
    {"id": "CHECKOUT-3967", "title": "Checkout scenario 3967", "data": {"sku": "SKU3967", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3967@example.com", "threshold": 670}},
    {"id": "CHECKOUT-3968", "title": "Checkout scenario 3968", "data": {"sku": "SKU3968", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3968@example.com", "threshold": 680}},
    {"id": "CHECKOUT-3969", "title": "Checkout scenario 3969", "data": {"sku": "SKU3969", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3969@example.com", "threshold": 690}},
    {"id": "CHECKOUT-3970", "title": "Checkout scenario 3970", "data": {"sku": "SKU3970", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3970@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
