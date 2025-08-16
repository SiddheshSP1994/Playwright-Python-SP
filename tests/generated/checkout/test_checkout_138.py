import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-8221", "title": "Checkout scenario 8221", "data": {"sku": "SKU8221", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8221@example.com", "threshold": 210}},
    {"id": "CHECKOUT-8222", "title": "Checkout scenario 8222", "data": {"sku": "SKU8222", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8222@example.com", "threshold": 220}},
    {"id": "CHECKOUT-8223", "title": "Checkout scenario 8223", "data": {"sku": "SKU8223", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8223@example.com", "threshold": 230}},
    {"id": "CHECKOUT-8224", "title": "Checkout scenario 8224", "data": {"sku": "SKU8224", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8224@example.com", "threshold": 240}},
    {"id": "CHECKOUT-8225", "title": "Checkout scenario 8225", "data": {"sku": "SKU8225", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8225@example.com", "threshold": 250}},
    {"id": "CHECKOUT-8226", "title": "Checkout scenario 8226", "data": {"sku": "SKU8226", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8226@example.com", "threshold": 260}},
    {"id": "CHECKOUT-8227", "title": "Checkout scenario 8227", "data": {"sku": "SKU8227", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8227@example.com", "threshold": 270}},
    {"id": "CHECKOUT-8228", "title": "Checkout scenario 8228", "data": {"sku": "SKU8228", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8228@example.com", "threshold": 280}},
    {"id": "CHECKOUT-8229", "title": "Checkout scenario 8229", "data": {"sku": "SKU8229", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8229@example.com", "threshold": 290}},
    {"id": "CHECKOUT-8230", "title": "Checkout scenario 8230", "data": {"sku": "SKU8230", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8230@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
