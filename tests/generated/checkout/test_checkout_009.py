import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-0481", "title": "Checkout scenario 481", "data": {"sku": "SKU481", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user481@example.com", "threshold": 810}},
    {"id": "CHECKOUT-0482", "title": "Checkout scenario 482", "data": {"sku": "SKU482", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user482@example.com", "threshold": 820}},
    {"id": "CHECKOUT-0483", "title": "Checkout scenario 483", "data": {"sku": "SKU483", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user483@example.com", "threshold": 830}},
    {"id": "CHECKOUT-0484", "title": "Checkout scenario 484", "data": {"sku": "SKU484", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user484@example.com", "threshold": 840}},
    {"id": "CHECKOUT-0485", "title": "Checkout scenario 485", "data": {"sku": "SKU485", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user485@example.com", "threshold": 850}},
    {"id": "CHECKOUT-0486", "title": "Checkout scenario 486", "data": {"sku": "SKU486", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user486@example.com", "threshold": 860}},
    {"id": "CHECKOUT-0487", "title": "Checkout scenario 487", "data": {"sku": "SKU487", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user487@example.com", "threshold": 870}},
    {"id": "CHECKOUT-0488", "title": "Checkout scenario 488", "data": {"sku": "SKU488", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user488@example.com", "threshold": 880}},
    {"id": "CHECKOUT-0489", "title": "Checkout scenario 489", "data": {"sku": "SKU489", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user489@example.com", "threshold": 890}},
    {"id": "CHECKOUT-0490", "title": "Checkout scenario 490", "data": {"sku": "SKU490", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user490@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
