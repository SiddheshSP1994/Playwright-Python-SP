import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-0721", "title": "Checkout scenario 721", "data": {"sku": "SKU721", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user721@example.com", "threshold": 210}},
    {"id": "CHECKOUT-0722", "title": "Checkout scenario 722", "data": {"sku": "SKU722", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user722@example.com", "threshold": 220}},
    {"id": "CHECKOUT-0723", "title": "Checkout scenario 723", "data": {"sku": "SKU723", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user723@example.com", "threshold": 230}},
    {"id": "CHECKOUT-0724", "title": "Checkout scenario 724", "data": {"sku": "SKU724", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user724@example.com", "threshold": 240}},
    {"id": "CHECKOUT-0725", "title": "Checkout scenario 725", "data": {"sku": "SKU725", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user725@example.com", "threshold": 250}},
    {"id": "CHECKOUT-0726", "title": "Checkout scenario 726", "data": {"sku": "SKU726", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user726@example.com", "threshold": 260}},
    {"id": "CHECKOUT-0727", "title": "Checkout scenario 727", "data": {"sku": "SKU727", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user727@example.com", "threshold": 270}},
    {"id": "CHECKOUT-0728", "title": "Checkout scenario 728", "data": {"sku": "SKU728", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user728@example.com", "threshold": 280}},
    {"id": "CHECKOUT-0729", "title": "Checkout scenario 729", "data": {"sku": "SKU729", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user729@example.com", "threshold": 290}},
    {"id": "CHECKOUT-0730", "title": "Checkout scenario 730", "data": {"sku": "SKU730", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user730@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
