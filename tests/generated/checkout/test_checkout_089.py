import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-5281", "title": "Checkout scenario 5281", "data": {"sku": "SKU5281", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5281@example.com", "threshold": 810}},
    {"id": "CHECKOUT-5282", "title": "Checkout scenario 5282", "data": {"sku": "SKU5282", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5282@example.com", "threshold": 820}},
    {"id": "CHECKOUT-5283", "title": "Checkout scenario 5283", "data": {"sku": "SKU5283", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5283@example.com", "threshold": 830}},
    {"id": "CHECKOUT-5284", "title": "Checkout scenario 5284", "data": {"sku": "SKU5284", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5284@example.com", "threshold": 840}},
    {"id": "CHECKOUT-5285", "title": "Checkout scenario 5285", "data": {"sku": "SKU5285", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5285@example.com", "threshold": 850}},
    {"id": "CHECKOUT-5286", "title": "Checkout scenario 5286", "data": {"sku": "SKU5286", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5286@example.com", "threshold": 860}},
    {"id": "CHECKOUT-5287", "title": "Checkout scenario 5287", "data": {"sku": "SKU5287", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5287@example.com", "threshold": 870}},
    {"id": "CHECKOUT-5288", "title": "Checkout scenario 5288", "data": {"sku": "SKU5288", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5288@example.com", "threshold": 880}},
    {"id": "CHECKOUT-5289", "title": "Checkout scenario 5289", "data": {"sku": "SKU5289", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5289@example.com", "threshold": 890}},
    {"id": "CHECKOUT-5290", "title": "Checkout scenario 5290", "data": {"sku": "SKU5290", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5290@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
