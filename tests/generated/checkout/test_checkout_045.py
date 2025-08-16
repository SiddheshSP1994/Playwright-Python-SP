import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-2641", "title": "Checkout scenario 2641", "data": {"sku": "SKU2641", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2641@example.com", "threshold": 410}},
    {"id": "CHECKOUT-2642", "title": "Checkout scenario 2642", "data": {"sku": "SKU2642", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2642@example.com", "threshold": 420}},
    {"id": "CHECKOUT-2643", "title": "Checkout scenario 2643", "data": {"sku": "SKU2643", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2643@example.com", "threshold": 430}},
    {"id": "CHECKOUT-2644", "title": "Checkout scenario 2644", "data": {"sku": "SKU2644", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2644@example.com", "threshold": 440}},
    {"id": "CHECKOUT-2645", "title": "Checkout scenario 2645", "data": {"sku": "SKU2645", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2645@example.com", "threshold": 450}},
    {"id": "CHECKOUT-2646", "title": "Checkout scenario 2646", "data": {"sku": "SKU2646", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2646@example.com", "threshold": 460}},
    {"id": "CHECKOUT-2647", "title": "Checkout scenario 2647", "data": {"sku": "SKU2647", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2647@example.com", "threshold": 470}},
    {"id": "CHECKOUT-2648", "title": "Checkout scenario 2648", "data": {"sku": "SKU2648", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2648@example.com", "threshold": 480}},
    {"id": "CHECKOUT-2649", "title": "Checkout scenario 2649", "data": {"sku": "SKU2649", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2649@example.com", "threshold": 490}},
    {"id": "CHECKOUT-2650", "title": "Checkout scenario 2650", "data": {"sku": "SKU2650", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2650@example.com", "threshold": 500}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
