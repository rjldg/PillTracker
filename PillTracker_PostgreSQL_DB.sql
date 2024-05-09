--
-- PostgreSQL database dump
--

-- Dumped from database version 14.11
-- Dumped by pg_dump version 16.2

-- Started on 2024-05-09 14:13:19

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
-- TOC entry 5 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO postgres;

--
-- TOC entry 215 (class 1255 OID 16433)
-- Name: createpill(bigint, character varying, integer, integer, text); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.createpill(IN user_id bigint, IN pill_name character varying, IN pill_total_amt integer, IN pill_daily_intake integer, IN pill_notes text)
    LANGUAGE sql
    AS $$INSERT INTO "Pills" VALUES (
	DEFAULT,
	user_id,
	pill_name,
	pill_total_amt,
	pill_daily_intake,
	DEFAULT,
	pill_notes
);$$;


ALTER PROCEDURE public.createpill(IN user_id bigint, IN pill_name character varying, IN pill_total_amt integer, IN pill_daily_intake integer, IN pill_notes text) OWNER TO postgres;

--
-- TOC entry 216 (class 1255 OID 16434)
-- Name: createuser(character varying, character varying, character varying, character varying, character varying, character varying); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.createuser(IN first_name character varying, IN last_name character varying, IN username character varying, IN email character varying, IN password character varying, IN gender character varying)
    LANGUAGE sql
    AS $$INSERT INTO "PillTracker_User" VALUES (
	DEFAULT,
	first_name,
	last_name,
	username,
	email,
	password,
	gender
);$$;


ALTER PROCEDURE public.createuser(IN first_name character varying, IN last_name character varying, IN username character varying, IN email character varying, IN password character varying, IN gender character varying) OWNER TO postgres;

--
-- TOC entry 217 (class 1255 OID 16435)
-- Name: decrement_pills_taken(bigint, date); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.decrement_pills_taken(pill_id bigint, date_today date) RETURNS integer
    LANGUAGE plpgsql
    AS $$
DECLARE 
	prev_intake INTEGER;
	new_intake INTEGER;
 
BEGIN
	SELECT "Pills_Taken" INTO prev_intake FROM "Pills" WHERE "Pill_ID" = pill_id;

	new_intake := prev_intake - 1;

	UPDATE "Pills" SET "Pills_Taken" = new_intake WHERE "Pill_ID" = pill_id;

	CALL upsertstatistic(date_today, pill_id, -1);
	
  	RETURN new_intake;
END
$$;


ALTER FUNCTION public.decrement_pills_taken(pill_id bigint, date_today date) OWNER TO postgres;

--
-- TOC entry 218 (class 1255 OID 16436)
-- Name: increment_pills_taken(bigint, date); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.increment_pills_taken(pill_id bigint, date_today date) RETURNS integer
    LANGUAGE plpgsql
    AS $$
DECLARE 
	prev_intake INTEGER;
	new_intake INTEGER;
 
BEGIN
	SELECT "Pills_Taken" INTO prev_intake FROM "Pills" WHERE "Pill_ID" = pill_id;

	new_intake := prev_intake + 1;

	UPDATE "Pills" SET "Pills_Taken" = new_intake WHERE "Pill_ID" = pill_id;

	CALL upsertstatistic(date_today, pill_id, 1);
	
  	RETURN new_intake;
END
$$;


ALTER FUNCTION public.increment_pills_taken(pill_id bigint, date_today date) OWNER TO postgres;

--
-- TOC entry 231 (class 1255 OID 16437)
-- Name: upsertstatistic(date, bigint, integer); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.upsertstatistic(IN date_today date, IN pill_id bigint, IN operation integer)
    LANGUAGE plpgsql
    AS $$
DECLARE
	pills_taken INTEGER;
	pill_daily_intake INTEGER;
	pills_taken_stat INTEGER;

BEGIN
	SELECT "Pills_Taken" INTO pills_taken FROM "Pills" WHERE "Pill_ID" = pill_id;

	SELECT "Pill_Daily_Intake" INTO pill_daily_intake FROM "Pills" WHERE "Pill_ID" = pill_id;

	IF EXISTS (
        SELECT 1 FROM "PillTracker_Statistics"
        WHERE "Pill_Date_Taken" = date_today
          AND "Pill_ID" = pill_id
    ) THEN

		SELECT "Pills_Taken" INTO pills_taken_stat FROM "PillTracker_Statistics" WHERE "Pill_ID" = pill_id;
		
		IF (pills_taken_stat + operation >= 0) THEN
		    UPDATE "PillTracker_Statistics" SET "Pills_Taken" = "Pills_Taken" + operation
        	WHERE "Pill_Date_Taken" = date_today AND "Pill_ID" = pill_id;
  		END IF;

    ELSE
        
		IF (0 + operation >= 0) THEN
		    INSERT INTO "PillTracker_Statistics" VALUES (DEFAULT, pill_id, date_today, 0 + operation, pill_daily_intake);
  		END IF;
		
    END IF;
/*
	INSERT INTO "PillTracker_Statistics" VALUES (
		DEFAULT,
		pill_id,
		date_today,
		pills_taken,
		pill_daily_intake
	) ON CONFLICT ("Pill_Date_Taken", "Pill_ID")
		WHERE "Pill_ID" IS NOT NULL
		DO UPDATE SET 
		"Pills_Taken" = pills_taken,
		"Pill_Daily_Intake" = pill_daily_intake;
*/

END;
$$;


ALTER PROCEDURE public.upsertstatistic(IN date_today date, IN pill_id bigint, IN operation integer) OWNER TO postgres;

--
-- TOC entry 228 (class 1255 OID 16438)
-- Name: validate_login(character varying, character varying); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.validate_login(username character varying, pw_input character varying) RETURNS smallint
    LANGUAGE plpgsql
    AS $$DECLARE
  pw_secure VARCHAR;
BEGIN
  SELECT "Password" INTO pw_secure FROM "PillTracker_User"
  WHERE "Username" = username;

  IF FOUND THEN 
    IF pw_input = pw_secure THEN
      RETURN 1;
    ELSE
      RETURN 0;
    END IF;
  ELSE
    RETURN 0;
  END IF;
END;
$$;


ALTER FUNCTION public.validate_login(username character varying, pw_input character varying) OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 209 (class 1259 OID 16439)
-- Name: PillTracker_Statistics; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."PillTracker_Statistics" (
    "Pill_Stat_ID" bigint NOT NULL,
    "Pill_ID" bigint NOT NULL,
    "Pill_Date_Taken" date NOT NULL,
    "Pills_Taken" integer NOT NULL,
    "Pill_Daily_Intake" integer NOT NULL
);


ALTER TABLE public."PillTracker_Statistics" OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 16442)
-- Name: PillTracker_Statistics_Pill_Stat_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."PillTracker_Statistics_Pill_Stat_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."PillTracker_Statistics_Pill_Stat_ID_seq" OWNER TO postgres;

--
-- TOC entry 4316 (class 0 OID 0)
-- Dependencies: 210
-- Name: PillTracker_Statistics_Pill_Stat_ID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."PillTracker_Statistics_Pill_Stat_ID_seq" OWNED BY public."PillTracker_Statistics"."Pill_Stat_ID";


--
-- TOC entry 211 (class 1259 OID 16443)
-- Name: PillTracker_User; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."PillTracker_User" (
    "User_ID" bigint NOT NULL,
    "First_Name" character varying(128) NOT NULL,
    "Last_Name" character varying(128) NOT NULL,
    "Username" character varying(128) NOT NULL,
    "Email" character varying(128) NOT NULL,
    "Password" character varying(128) NOT NULL,
    "Gender" character varying(128) NOT NULL
);


ALTER TABLE public."PillTracker_User" OWNER TO postgres;

--
-- TOC entry 4317 (class 0 OID 0)
-- Dependencies: 211
-- Name: TABLE "PillTracker_User"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."PillTracker_User" IS 'Table for PillTracker Users';


--
-- TOC entry 212 (class 1259 OID 16448)
-- Name: PillTracker_User_User_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."PillTracker_User_User_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."PillTracker_User_User_ID_seq" OWNER TO postgres;

--
-- TOC entry 4318 (class 0 OID 0)
-- Dependencies: 212
-- Name: PillTracker_User_User_ID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."PillTracker_User_User_ID_seq" OWNED BY public."PillTracker_User"."User_ID";


--
-- TOC entry 213 (class 1259 OID 16449)
-- Name: Pills; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Pills" (
    "Pill_ID" bigint NOT NULL,
    "User_ID" bigint NOT NULL,
    "Pill_Name" character varying(128) NOT NULL,
    "Pill_Total_Amount" integer NOT NULL,
    "Pill_Daily_Intake" integer NOT NULL,
    "Pills_Taken" integer DEFAULT 0 NOT NULL,
    "Pill_Notes" text
);


ALTER TABLE public."Pills" OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16455)
-- Name: Pills_Pill_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Pills_Pill_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."Pills_Pill_ID_seq" OWNER TO postgres;

--
-- TOC entry 4319 (class 0 OID 0)
-- Dependencies: 214
-- Name: Pills_Pill_ID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Pills_Pill_ID_seq" OWNED BY public."Pills"."Pill_ID";


--
-- TOC entry 4143 (class 2604 OID 16485)
-- Name: PillTracker_Statistics Pill_Stat_ID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PillTracker_Statistics" ALTER COLUMN "Pill_Stat_ID" SET DEFAULT nextval('public."PillTracker_Statistics_Pill_Stat_ID_seq"'::regclass);


--
-- TOC entry 4144 (class 2604 OID 16486)
-- Name: PillTracker_User User_ID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PillTracker_User" ALTER COLUMN "User_ID" SET DEFAULT nextval('public."PillTracker_User_User_ID_seq"'::regclass);


--
-- TOC entry 4145 (class 2604 OID 16487)
-- Name: Pills Pill_ID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Pills" ALTER COLUMN "Pill_ID" SET DEFAULT nextval('public."Pills_Pill_ID_seq"'::regclass);


--
-- TOC entry 4304 (class 0 OID 16439)
-- Dependencies: 209
-- Data for Name: PillTracker_Statistics; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."PillTracker_Statistics" ("Pill_Stat_ID", "Pill_ID", "Pill_Date_Taken", "Pills_Taken", "Pill_Daily_Intake") FROM stdin;
31	1	2024-04-12	2	2
30	1	2024-04-11	2	2
32	4	2024-04-12	2	3
33	4	2024-04-13	1	3
44	14	2024-05-09	1	2
46	1	2024-05-09	0	2
37	4	2024-05-08	2	3
34	5	2024-05-08	8	4
36	1	2024-05-08	2	2
41	5	2024-05-09	3	4
\.


--
-- TOC entry 4306 (class 0 OID 16443)
-- Dependencies: 211
-- Data for Name: PillTracker_User; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."PillTracker_User" ("User_ID", "First_Name", "Last_Name", "Username", "Email", "Password", "Gender") FROM stdin;
4	Marvin	Lee	mvlee	marvslee@gmail.com	marvschadlee	Male
3	Dionis	Padilla	pads	dapadilla@gmail.com	reevespogi	Male
2	Jaypee	Cruz	jptcruz	jptcruz@mymail.mapua.edu.ph	waffle	Male
21	Floro	Llacuna	floro	florolacs@gmail.com	calc3	Male
22	Dan Andrew	Magcuyao	mags	dahmagcuyao@gmail.com	edamags	Male
24	Francis	Llacuna	francis	francislax@gmaial.com	calc2	Male
\.


--
-- TOC entry 4308 (class 0 OID 16449)
-- Dependencies: 213
-- Data for Name: Pills; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Pills" ("Pill_ID", "User_ID", "Pill_Name", "Pill_Total_Amount", "Pill_Daily_Intake", "Pills_Taken", "Pill_Notes") FROM stdin;
4	3	Allopurinol	100	3	5	Take three times a day
5	2	Co-Amixoclav	20	4	3	\N
14	2	Marvizol	50	2	1	NULL
1	2	Solmux	50	2	0	Take two times a day
\.


--
-- TOC entry 4320 (class 0 OID 0)
-- Dependencies: 210
-- Name: PillTracker_Statistics_Pill_Stat_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."PillTracker_Statistics_Pill_Stat_ID_seq"', 46, true);


--
-- TOC entry 4321 (class 0 OID 0)
-- Dependencies: 212
-- Name: PillTracker_User_User_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."PillTracker_User_User_ID_seq"', 25, true);


--
-- TOC entry 4322 (class 0 OID 0)
-- Dependencies: 214
-- Name: Pills_Pill_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Pills_Pill_ID_seq"', 18, true);


--
-- TOC entry 4148 (class 2606 OID 16459)
-- Name: PillTracker_User Email_Check; Type: CHECK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE public."PillTracker_User"
    ADD CONSTRAINT "Email_Check" CHECK ((("Email")::text ~~ '%@%.%'::text)) NOT VALID;


--
-- TOC entry 4156 (class 2606 OID 16461)
-- Name: PillTracker_User Email_UQ; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PillTracker_User"
    ADD CONSTRAINT "Email_UQ" UNIQUE ("Email");


--
-- TOC entry 4149 (class 2606 OID 16462)
-- Name: PillTracker_User Gender_Check; Type: CHECK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE public."PillTracker_User"
    ADD CONSTRAINT "Gender_Check" CHECK ((("Gender")::text = ANY (ARRAY[('Male'::character varying)::text, ('Female'::character varying)::text]))) NOT VALID;


--
-- TOC entry 4153 (class 2606 OID 16464)
-- Name: PillTracker_Statistics PillTracker_Statistics_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PillTracker_Statistics"
    ADD CONSTRAINT "PillTracker_Statistics_pkey" PRIMARY KEY ("Pill_Stat_ID");


--
-- TOC entry 4158 (class 2606 OID 16466)
-- Name: PillTracker_User PillTracker_User_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PillTracker_User"
    ADD CONSTRAINT "PillTracker_User_pkey" PRIMARY KEY ("User_ID");


--
-- TOC entry 4147 (class 2606 OID 16467)
-- Name: PillTracker_Statistics Pills_Taken_Check; Type: CHECK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE public."PillTracker_Statistics"
    ADD CONSTRAINT "Pills_Taken_Check" CHECK (("Pills_Taken" >= 0)) NOT VALID;


--
-- TOC entry 4150 (class 2606 OID 16468)
-- Name: Pills Pills_Taken_Check; Type: CHECK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE public."Pills"
    ADD CONSTRAINT "Pills_Taken_Check" CHECK (("Pills_Taken" >= 0)) NOT VALID;


--
-- TOC entry 4151 (class 2606 OID 16469)
-- Name: Pills Pills_Taken_TotalAmt_Check; Type: CHECK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE public."Pills"
    ADD CONSTRAINT "Pills_Taken_TotalAmt_Check" CHECK (("Pills_Taken" <= "Pill_Total_Amount")) NOT VALID;


--
-- TOC entry 4162 (class 2606 OID 16471)
-- Name: Pills Pills_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Pills"
    ADD CONSTRAINT "Pills_pkey" PRIMARY KEY ("Pill_ID");


--
-- TOC entry 4160 (class 2606 OID 16473)
-- Name: PillTracker_User Username_UQ; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PillTracker_User"
    ADD CONSTRAINT "Username_UQ" UNIQUE ("Username");


--
-- TOC entry 4154 (class 1259 OID 16474)
-- Name: date_pillid_unique_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX date_pillid_unique_idx ON public."PillTracker_Statistics" USING btree ("Pill_Date_Taken", "Pill_ID") WHERE ("Pill_ID" IS NOT NULL);


--
-- TOC entry 4163 (class 2606 OID 16475)
-- Name: PillTracker_Statistics Pill_ID_FK; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PillTracker_Statistics"
    ADD CONSTRAINT "Pill_ID_FK" FOREIGN KEY ("Pill_ID") REFERENCES public."Pills"("Pill_ID") ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 4164 (class 2606 OID 16480)
-- Name: Pills User_ID_FK; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Pills"
    ADD CONSTRAINT "User_ID_FK" FOREIGN KEY ("User_ID") REFERENCES public."PillTracker_User"("User_ID") ON DELETE CASCADE;


--
-- TOC entry 4315 (class 0 OID 0)
-- Dependencies: 5
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2024-05-09 14:13:23

--
-- PostgreSQL database dump complete
--

