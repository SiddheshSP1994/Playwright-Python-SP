import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-6241", "title": "Checkout scenario 6241", "data": {"sku": "SKU6241", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6241@example.com", "threshold": 410}},
    {"id": "CHECKOUT-6242", "title": "Checkout scenario 6242", "data": {"sku": "SKU6242", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6242@example.com", "threshold": 420}},
    {"id": "CHECKOUT-6243", "title": "Checkout scenario 6243", "data": {"sku": "SKU6243", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6243@example.com", "threshold": 430}},
    {"id": "CHECKOUT-6244", "title": "Checkout scenario 6244", "data": {"sku": "SKU6244", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6244@example.com", "threshold": 440}},
    {"id": "CHECKOUT-6245", "title": "Checkout scenario 6245", "data": {"sku": "SKU6245", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6245@example.com", "threshold": 450}},
    {"id": "CHECKOUT-6246", "title": "Checkout scenario 6246", "data": {"sku": "SKU6246", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6246@example.com", "threshold": 460}},
    {"id": "CHECKOUT-6247", "title": "Checkout scenario 6247", "data": {"sku": "SKU6247", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6247@example.com", "threshold": 470}},
    {"id": "CHECKOUT-6248", "title": "Checkout scenario 6248", "data": {"sku": "SKU6248", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6248@example.com", "threshold": 480}},
    {"id": "CHECKOUT-6249", "title": "Checkout scenario 6249", "data": {"sku": "SKU6249", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6249@example.com", "threshold": 490}},
    {"id": "CHECKOUT-6250", "title": "Checkout scenario 6250", "data": {"sku": "SKU6250", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6250@example.com", "threshold": 500}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
