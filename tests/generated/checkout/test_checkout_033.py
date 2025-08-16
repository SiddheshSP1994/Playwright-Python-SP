import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-1921", "title": "Checkout scenario 1921", "data": {"sku": "SKU1921", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1921@example.com", "threshold": 210}},
    {"id": "CHECKOUT-1922", "title": "Checkout scenario 1922", "data": {"sku": "SKU1922", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1922@example.com", "threshold": 220}},
    {"id": "CHECKOUT-1923", "title": "Checkout scenario 1923", "data": {"sku": "SKU1923", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1923@example.com", "threshold": 230}},
    {"id": "CHECKOUT-1924", "title": "Checkout scenario 1924", "data": {"sku": "SKU1924", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1924@example.com", "threshold": 240}},
    {"id": "CHECKOUT-1925", "title": "Checkout scenario 1925", "data": {"sku": "SKU1925", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1925@example.com", "threshold": 250}},
    {"id": "CHECKOUT-1926", "title": "Checkout scenario 1926", "data": {"sku": "SKU1926", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1926@example.com", "threshold": 260}},
    {"id": "CHECKOUT-1927", "title": "Checkout scenario 1927", "data": {"sku": "SKU1927", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1927@example.com", "threshold": 270}},
    {"id": "CHECKOUT-1928", "title": "Checkout scenario 1928", "data": {"sku": "SKU1928", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1928@example.com", "threshold": 280}},
    {"id": "CHECKOUT-1929", "title": "Checkout scenario 1929", "data": {"sku": "SKU1929", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1929@example.com", "threshold": 290}},
    {"id": "CHECKOUT-1930", "title": "Checkout scenario 1930", "data": {"sku": "SKU1930", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1930@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
