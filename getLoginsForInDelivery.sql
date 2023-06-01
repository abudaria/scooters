-- список логинов курьеров с количеством их заказов в статусе «В доставке»
SELECT c."login", COUNT(o."id") AS "OrdersCount"
FROM "Couriers" c
JOIN "Orders" o ON c."id" = o."courierId"
WHERE o."inDelivery" = TRUE
GROUP BY c."login";