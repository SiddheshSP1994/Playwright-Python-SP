import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-2581", "title": "Checkout scenario 2581", "data": {"sku": "SKU2581", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2581@example.com", "threshold": 810}},
    {"id": "CHECKOUT-2582", "title": "Checkout scenario 2582", "data": {"sku": "SKU2582", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2582@example.com", "threshold": 820}},
    {"id": "CHECKOUT-2583", "title": "Checkout scenario 2583", "data": {"sku": "SKU2583", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2583@example.com", "threshold": 830}},
    {"id": "CHECKOUT-2584", "title": "Checkout scenario 2584", "data": {"sku": "SKU2584", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2584@example.com", "threshold": 840}},
    {"id": "CHECKOUT-2585", "title": "Checkout scenario 2585", "data": {"sku": "SKU2585", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2585@example.com", "threshold": 850}},
    {"id": "CHECKOUT-2586", "title": "Checkout scenario 2586", "data": {"sku": "SKU2586", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2586@example.com", "threshold": 860}},
    {"id": "CHECKOUT-2587", "title": "Checkout scenario 2587", "data": {"sku": "SKU2587", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2587@example.com", "threshold": 870}},
    {"id": "CHECKOUT-2588", "title": "Checkout scenario 2588", "data": {"sku": "SKU2588", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2588@example.com", "threshold": 880}},
    {"id": "CHECKOUT-2589", "title": "Checkout scenario 2589", "data": {"sku": "SKU2589", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2589@example.com", "threshold": 890}},
    {"id": "CHECKOUT-2590", "title": "Checkout scenario 2590", "data": {"sku": "SKU2590", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2590@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
