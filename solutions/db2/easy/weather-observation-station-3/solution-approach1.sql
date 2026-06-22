-- ──────────────────────────────────────────────────
-- Problem     Weather Observation Station 3
-- Difficulty  Easy
-- Subdomain   Basic Select
-- Platform    HackerRank
-- Language    db2
-- Status      Accepted
-- Submitted   2026-06-22, 03:56 p.m.
-- ──────────────────────────────────────────────────

SELECT DISTINCT CITY FROM STATION WHERE MOD(ID, 2)=0;
