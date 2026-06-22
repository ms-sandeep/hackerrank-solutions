-- ──────────────────────────────────────────────────
-- Problem     Weather Observation Station 4
-- Difficulty  Easy
-- Subdomain   Basic Select
-- Platform    HackerRank
-- Language    db2
-- Status      Accepted
-- Submitted   2026-06-22, 04:31 p.m.
-- ──────────────────────────────────────────────────

SELECT COUNT(CITY)-COUNT(DISTINCT CITY) 
FROM STATION;
