import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-0241", "title": "Checkout scenario 241", "data": {"sku": "SKU241", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user241@example.com", "threshold": 410}},
    {"id": "CHECKOUT-0242", "title": "Checkout scenario 242", "data": {"sku": "SKU242", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user242@example.com", "threshold": 420}},
    {"id": "CHECKOUT-0243", "title": "Checkout scenario 243", "data": {"sku": "SKU243", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user243@example.com", "threshold": 430}},
    {"id": "CHECKOUT-0244", "title": "Checkout scenario 244", "data": {"sku": "SKU244", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user244@example.com", "threshold": 440}},
    {"id": "CHECKOUT-0245", "title": "Checkout scenario 245", "data": {"sku": "SKU245", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user245@example.com", "threshold": 450}},
    {"id": "CHECKOUT-0246", "title": "Checkout scenario 246", "data": {"sku": "SKU246", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user246@example.com", "threshold": 460}},
    {"id": "CHECKOUT-0247", "title": "Checkout scenario 247", "data": {"sku": "SKU247", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user247@example.com", "threshold": 470}},
    {"id": "CHECKOUT-0248", "title": "Checkout scenario 248", "data": {"sku": "SKU248", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user248@example.com", "threshold": 480}},
    {"id": "CHECKOUT-0249", "title": "Checkout scenario 249", "data": {"sku": "SKU249", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user249@example.com", "threshold": 490}},
    {"id": "CHECKOUT-0250", "title": "Checkout scenario 250", "data": {"sku": "SKU250", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user250@example.com", "threshold": 500}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
