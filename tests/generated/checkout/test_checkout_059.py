import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-3481", "title": "Checkout scenario 3481", "data": {"sku": "SKU3481", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3481@example.com", "threshold": 810}},
    {"id": "CHECKOUT-3482", "title": "Checkout scenario 3482", "data": {"sku": "SKU3482", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3482@example.com", "threshold": 820}},
    {"id": "CHECKOUT-3483", "title": "Checkout scenario 3483", "data": {"sku": "SKU3483", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3483@example.com", "threshold": 830}},
    {"id": "CHECKOUT-3484", "title": "Checkout scenario 3484", "data": {"sku": "SKU3484", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3484@example.com", "threshold": 840}},
    {"id": "CHECKOUT-3485", "title": "Checkout scenario 3485", "data": {"sku": "SKU3485", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3485@example.com", "threshold": 850}},
    {"id": "CHECKOUT-3486", "title": "Checkout scenario 3486", "data": {"sku": "SKU3486", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3486@example.com", "threshold": 860}},
    {"id": "CHECKOUT-3487", "title": "Checkout scenario 3487", "data": {"sku": "SKU3487", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3487@example.com", "threshold": 870}},
    {"id": "CHECKOUT-3488", "title": "Checkout scenario 3488", "data": {"sku": "SKU3488", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3488@example.com", "threshold": 880}},
    {"id": "CHECKOUT-3489", "title": "Checkout scenario 3489", "data": {"sku": "SKU3489", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3489@example.com", "threshold": 890}},
    {"id": "CHECKOUT-3490", "title": "Checkout scenario 3490", "data": {"sku": "SKU3490", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3490@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
