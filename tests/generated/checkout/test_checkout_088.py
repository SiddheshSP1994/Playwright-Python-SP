import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-5221", "title": "Checkout scenario 5221", "data": {"sku": "SKU5221", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5221@example.com", "threshold": 210}},
    {"id": "CHECKOUT-5222", "title": "Checkout scenario 5222", "data": {"sku": "SKU5222", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5222@example.com", "threshold": 220}},
    {"id": "CHECKOUT-5223", "title": "Checkout scenario 5223", "data": {"sku": "SKU5223", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5223@example.com", "threshold": 230}},
    {"id": "CHECKOUT-5224", "title": "Checkout scenario 5224", "data": {"sku": "SKU5224", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5224@example.com", "threshold": 240}},
    {"id": "CHECKOUT-5225", "title": "Checkout scenario 5225", "data": {"sku": "SKU5225", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5225@example.com", "threshold": 250}},
    {"id": "CHECKOUT-5226", "title": "Checkout scenario 5226", "data": {"sku": "SKU5226", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5226@example.com", "threshold": 260}},
    {"id": "CHECKOUT-5227", "title": "Checkout scenario 5227", "data": {"sku": "SKU5227", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5227@example.com", "threshold": 270}},
    {"id": "CHECKOUT-5228", "title": "Checkout scenario 5228", "data": {"sku": "SKU5228", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5228@example.com", "threshold": 280}},
    {"id": "CHECKOUT-5229", "title": "Checkout scenario 5229", "data": {"sku": "SKU5229", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5229@example.com", "threshold": 290}},
    {"id": "CHECKOUT-5230", "title": "Checkout scenario 5230", "data": {"sku": "SKU5230", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5230@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
