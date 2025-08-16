import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-2001", "title": "Orders scenario 2001", "data": {"sku": "SKU2001", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2001@example.com", "threshold": 10}},
    {"id": "ORDERS-2002", "title": "Orders scenario 2002", "data": {"sku": "SKU2002", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2002@example.com", "threshold": 20}},
    {"id": "ORDERS-2003", "title": "Orders scenario 2003", "data": {"sku": "SKU2003", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2003@example.com", "threshold": 30}},
    {"id": "ORDERS-2004", "title": "Orders scenario 2004", "data": {"sku": "SKU2004", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2004@example.com", "threshold": 40}},
    {"id": "ORDERS-2005", "title": "Orders scenario 2005", "data": {"sku": "SKU2005", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2005@example.com", "threshold": 50}},
    {"id": "ORDERS-2006", "title": "Orders scenario 2006", "data": {"sku": "SKU2006", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2006@example.com", "threshold": 60}},
    {"id": "ORDERS-2007", "title": "Orders scenario 2007", "data": {"sku": "SKU2007", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2007@example.com", "threshold": 70}},
    {"id": "ORDERS-2008", "title": "Orders scenario 2008", "data": {"sku": "SKU2008", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2008@example.com", "threshold": 80}},
    {"id": "ORDERS-2009", "title": "Orders scenario 2009", "data": {"sku": "SKU2009", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2009@example.com", "threshold": 90}},
    {"id": "ORDERS-2010", "title": "Orders scenario 2010", "data": {"sku": "SKU2010", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2010@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
