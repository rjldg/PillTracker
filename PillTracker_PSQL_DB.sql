--
-- PostgreSQL database dump
--

-- Dumped from database version 14.11 (Ubuntu 14.11-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 16.2

-- Started on 2024-04-20 10:13:29

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3347 (class 1262 OID 24576)
-- Name: PillTracker; Type: DATABASE; Schema: -; Owner: sa
--

CREATE DATABASE "PillTracker" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'C.UTF-8';


ALTER DATABASE "PillTracker" OWNER TO sa;

\connect "PillTracker"

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3336 (class 0 OID 24578)
-- Dependencies: 209
-- Data for Name: PillTracker_User; Type: TABLE DATA; Schema: public; Owner: sa
--

INSERT INTO public."PillTracker_User" ("User_ID", "First_Name", "Last_Name", "Username", "Email", "Password", "Gender") OVERRIDING SYSTEM VALUE VALUES (2, 'John', 'Paul', 'jpcruz', 'jptcruz@gmail.com', 'waffle', 'Male') ON CONFLICT DO NOTHING;
INSERT INTO public."PillTracker_User" ("User_ID", "First_Name", "Last_Name", "Username", "Email", "Password", "Gender") OVERRIDING SYSTEM VALUE VALUES (3, 'Dionis', 'Padilla', 'pads', 'dapadilla@gmail.com', 'sshkeyjin', 'Male') ON CONFLICT DO NOTHING;
INSERT INTO public."PillTracker_User" ("User_ID", "First_Name", "Last_Name", "Username", "Email", "Password", "Gender") OVERRIDING SYSTEM VALUE VALUES (4, 'Marvin', 'Lee', 'mvlee', 'marvslee@gmail.com', 'marvschadlee', 'Male') ON CONFLICT DO NOTHING;
INSERT INTO public."PillTracker_User" ("User_ID", "First_Name", "Last_Name", "Username", "Email", "Password", "Gender") OVERRIDING SYSTEM VALUE VALUES (12, 'Carlos', 'Hortinela', 'horti4', 'cchortinelaiv@gmail.com', 'discreteMATH', 'Male') ON CONFLICT DO NOTHING;


--
-- TOC entry 3339 (class 0 OID 24640)
-- Dependencies: 212
-- Data for Name: Pills; Type: TABLE DATA; Schema: public; Owner: sa
--

INSERT INTO public."Pills" ("Pill_ID", "User_ID", "Pill_Name", "Pill_Total_Amount", "Pill_Daily_Intake", "Pills_Taken", "Pill_Notes") VALUES (5, 2, 'Co-Amixoclav', 20, 4, 0, NULL) ON CONFLICT DO NOTHING;
INSERT INTO public."Pills" ("Pill_ID", "User_ID", "Pill_Name", "Pill_Total_Amount", "Pill_Daily_Intake", "Pills_Taken", "Pill_Notes") VALUES (8, 12, 'Adderal', 30, 1, 0, 'To improve focus and attention span') ON CONFLICT DO NOTHING;
INSERT INTO public."Pills" ("Pill_ID", "User_ID", "Pill_Name", "Pill_Total_Amount", "Pill_Daily_Intake", "Pills_Taken", "Pill_Notes") VALUES (10, 12, 'Biogesic', 10, 2, 0, NULL) ON CONFLICT DO NOTHING;
INSERT INTO public."Pills" ("Pill_ID", "User_ID", "Pill_Name", "Pill_Total_Amount", "Pill_Daily_Intake", "Pills_Taken", "Pill_Notes") VALUES (1, 2, 'Solmux', 50, 2, 4, 'Take two times a day') ON CONFLICT DO NOTHING;
INSERT INTO public."Pills" ("Pill_ID", "User_ID", "Pill_Name", "Pill_Total_Amount", "Pill_Daily_Intake", "Pills_Taken", "Pill_Notes") VALUES (4, 3, 'Allopurinol', 100, 3, 3, 'For gout') ON CONFLICT DO NOTHING;


--
-- TOC entry 3341 (class 0 OID 32782)
-- Dependencies: 214
-- Data for Name: PillTracker_Statistics; Type: TABLE DATA; Schema: public; Owner: sa
--

INSERT INTO public."PillTracker_Statistics" ("Pill_Stat_ID", "Pill_ID", "Pill_Date_Taken", "Pills_Taken", "Pill_Daily_Intake") VALUES (31, 1, '2024-04-12', 2, 2) ON CONFLICT DO NOTHING;
INSERT INTO public."PillTracker_Statistics" ("Pill_Stat_ID", "Pill_ID", "Pill_Date_Taken", "Pills_Taken", "Pill_Daily_Intake") VALUES (30, 1, '2024-04-11', 2, 2) ON CONFLICT DO NOTHING;
INSERT INTO public."PillTracker_Statistics" ("Pill_Stat_ID", "Pill_ID", "Pill_Date_Taken", "Pills_Taken", "Pill_Daily_Intake") VALUES (32, 4, '2024-04-12', 2, 3) ON CONFLICT DO NOTHING;
INSERT INTO public."PillTracker_Statistics" ("Pill_Stat_ID", "Pill_ID", "Pill_Date_Taken", "Pills_Taken", "Pill_Daily_Intake") VALUES (33, 4, '2024-04-13', 1, 3) ON CONFLICT DO NOTHING;


--
-- TOC entry 3348 (class 0 OID 0)
-- Dependencies: 213
-- Name: PillTracker_Statistics_Pill_Stat_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: sa
--

SELECT pg_catalog.setval('public."PillTracker_Statistics_Pill_Stat_ID_seq"', 33, true);


--
-- TOC entry 3349 (class 0 OID 0)
-- Dependencies: 210
-- Name: PillTracker_User_User_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: sa
--

SELECT pg_catalog.setval('public."PillTracker_User_User_ID_seq"', 12, true);


--
-- TOC entry 3350 (class 0 OID 0)
-- Dependencies: 211
-- Name: Pills_Pill_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: sa
--

SELECT pg_catalog.setval('public."Pills_Pill_ID_seq"', 10, true);


-- Completed on 2024-04-20 10:13:29

--
-- PostgreSQL database dump complete
--

