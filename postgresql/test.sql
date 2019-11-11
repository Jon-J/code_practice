--
-- PostgreSQL database dump
--

-- Dumped from database version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)

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
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: branch; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.branch (
    branch_id integer NOT NULL,
    branch_name character varying(40),
    mgr_id integer,
    mgr_start_date date
);


ALTER TABLE public.branch OWNER TO postgres;

--
-- Name: branch_supplier; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.branch_supplier (
    branch_id integer NOT NULL,
    supplier_name character varying(40) NOT NULL,
    supply_type character varying(40)
);


ALTER TABLE public.branch_supplier OWNER TO postgres;

--
-- Name: client; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.client (
    client_id integer NOT NULL,
    client_name character varying(40),
    branch_id integer
);


ALTER TABLE public.client OWNER TO postgres;

--
-- Name: employee; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.employee (
    emp_id integer NOT NULL,
    first_name character varying(40),
    last_name character varying(40),
    birth_day date,
    sex character varying(1),
    salary integer,
    super_id integer,
    branch_id integer
);


ALTER TABLE public.employee OWNER TO postgres;

--
-- Name: student; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student (
    student_id integer NOT NULL,
    name character varying(20),
    major character varying(20)
);


ALTER TABLE public.student OWNER TO postgres;

--
-- Name: student_student_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.student_student_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.student_student_id_seq OWNER TO postgres;

--
-- Name: student_student_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.student_student_id_seq OWNED BY public.student.student_id;


--
-- Name: works_with; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.works_with (
    emp_id integer NOT NULL,
    client_id integer NOT NULL,
    total_sales integer
);


ALTER TABLE public.works_with OWNER TO postgres;

--
-- Name: student student_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student ALTER COLUMN student_id SET DEFAULT nextval('public.student_student_id_seq'::regclass);


--
-- Data for Name: branch; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.branch (branch_id, branch_name, mgr_id, mgr_start_date) FROM stdin;
1	Corporate	100	2006-02-09
2	Scranton	102	1992-04-06
3	Stamford	106	1998-02-13
\.


--
-- Data for Name: branch_supplier; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.branch_supplier (branch_id, supplier_name, supply_type) FROM stdin;
2	Hammer Mill	Paper
2	Uni-ball	Writing Utensils
3	Patriot Paper	Paper
2	J.T. Forms & Labels	Custom Forms
3	Uni-ball	Writing Utensils
3	Hammer Mill	Paper
3	Stamford Lables	Custom Forms
\.


--
-- Data for Name: client; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.client (client_id, client_name, branch_id) FROM stdin;
400	Dunmore Highschool	2
401	Lackawana Country	2
402	FedEx	3
403	John Daly Law, LLC	3
404	Scranton Whitepages	2
405	Times Newspaper	3
406	FedEx	2
\.


--
-- Data for Name: employee; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.employee (emp_id, first_name, last_name, birth_day, sex, salary, super_id, branch_id) FROM stdin;
100	David	Wallace	1967-11-17	M	250000	\N	1
101	Jan	Levinson	1961-05-11	F	110000	100	1
102	Michael	Scott	1964-03-15	M	75000	100	2
103	Angela	Martin	1971-06-25	F	63000	102	2
104	Kelly	Kapoor	1980-02-05	F	55000	102	2
105	Stanley	Hudson	1958-02-19	M	69000	102	2
106	Josh	Porter	1969-09-05	M	78000	100	3
107	Andy	Bernard	1973-07-22	M	65000	106	3
108	Jim	Halpert	1978-10-01	M	71000	106	3
\.


--
-- Data for Name: student; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student (student_id, name, major) FROM stdin;
7	user_1	Sociology
8	user_2	Sociology
9	user_3	Sociology
10	user_4	Sociology
11	user_5	Sociology
12	user_6	Chemistry
13	user_7	Sociology
14	user_8	Sociology
15	user_9	Sociology
16	user_10	Biology
17	dummy1	Chemistry
18	dummy2	Biology
19	dummy3	Sociology
20	yummy1	Biology
21	yummy2	Sociology
22	yummy3	Sociology
\.


--
-- Data for Name: works_with; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.works_with (emp_id, client_id, total_sales) FROM stdin;
105	400	55000
102	401	267000
108	402	22500
107	403	5000
108	403	12000
105	404	33000
107	405	26000
102	406	15000
105	406	130000
\.


--
-- Name: student_student_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.student_student_id_seq', 22, true);


--
-- Name: branch branch_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.branch
    ADD CONSTRAINT branch_pkey PRIMARY KEY (branch_id);


--
-- Name: branch_supplier branch_supplier_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.branch_supplier
    ADD CONSTRAINT branch_supplier_pkey PRIMARY KEY (branch_id, supplier_name);


--
-- Name: client client_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client
    ADD CONSTRAINT client_pkey PRIMARY KEY (client_id);


--
-- Name: employee employee_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_pkey PRIMARY KEY (emp_id);


--
-- Name: student student_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_pkey PRIMARY KEY (student_id);


--
-- Name: works_with works_with_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.works_with
    ADD CONSTRAINT works_with_pkey PRIMARY KEY (emp_id, client_id);


--
-- Name: branch branch_mgr_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.branch
    ADD CONSTRAINT branch_mgr_id_fkey FOREIGN KEY (mgr_id) REFERENCES public.employee(emp_id) ON DELETE SET NULL;


--
-- Name: branch_supplier branch_supplier_branch_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.branch_supplier
    ADD CONSTRAINT branch_supplier_branch_id_fkey FOREIGN KEY (branch_id) REFERENCES public.branch(branch_id) ON DELETE CASCADE;


--
-- Name: client client_branch_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client
    ADD CONSTRAINT client_branch_id_fkey FOREIGN KEY (branch_id) REFERENCES public.branch(branch_id) ON DELETE SET NULL;


--
-- Name: employee employee_branch_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_branch_id_fkey FOREIGN KEY (branch_id) REFERENCES public.branch(branch_id) ON DELETE SET NULL;


--
-- Name: employee employee_super_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_super_id_fkey FOREIGN KEY (super_id) REFERENCES public.employee(emp_id) ON DELETE SET NULL;


--
-- Name: works_with works_with_client_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.works_with
    ADD CONSTRAINT works_with_client_id_fkey FOREIGN KEY (client_id) REFERENCES public.client(client_id) ON DELETE CASCADE;


--
-- Name: works_with works_with_emp_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.works_with
    ADD CONSTRAINT works_with_emp_id_fkey FOREIGN KEY (emp_id) REFERENCES public.employee(emp_id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

