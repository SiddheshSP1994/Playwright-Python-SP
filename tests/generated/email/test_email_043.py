import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-2561", "title": "Email scenario 2561", "data": {"sku": "SKU2561", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2561@example.com", "threshold": 610}},
    {"id": "EMAIL-2562", "title": "Email scenario 2562", "data": {"sku": "SKU2562", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2562@example.com", "threshold": 620}},
    {"id": "EMAIL-2563", "title": "Email scenario 2563", "data": {"sku": "SKU2563", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2563@example.com", "threshold": 630}},
    {"id": "EMAIL-2564", "title": "Email scenario 2564", "data": {"sku": "SKU2564", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2564@example.com", "threshold": 640}},
    {"id": "EMAIL-2565", "title": "Email scenario 2565", "data": {"sku": "SKU2565", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2565@example.com", "threshold": 650}},
    {"id": "EMAIL-2566", "title": "Email scenario 2566", "data": {"sku": "SKU2566", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2566@example.com", "threshold": 660}},
    {"id": "EMAIL-2567", "title": "Email scenario 2567", "data": {"sku": "SKU2567", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2567@example.com", "threshold": 670}},
    {"id": "EMAIL-2568", "title": "Email scenario 2568", "data": {"sku": "SKU2568", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2568@example.com", "threshold": 680}},
    {"id": "EMAIL-2569", "title": "Email scenario 2569", "data": {"sku": "SKU2569", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2569@example.com", "threshold": 690}},
    {"id": "EMAIL-2570", "title": "Email scenario 2570", "data": {"sku": "SKU2570", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2570@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
