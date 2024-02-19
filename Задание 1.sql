SELECT c.login,
       COUNT(*)
FROM "Couriers" AS c
JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = TRUE
GROUP BY c."login";
