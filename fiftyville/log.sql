-- Keep a log of any SQL queries you execute as you solve the mystery.

SELECT description FROM crime_scene_reports WHERE month = 7 AND day = 28 AND street = 'Humphrey Street' -- Time of the rubarry 10:15am. There are 3 witnesses. Interview transcripts mention the bakery. Littering took place at 16:36

SELECT DISTINCT name FROM people JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate WHERE people.license_plate IN
(SELECT license_plate FROM bakery_security_logs WHERE month = 7 AND day = 28 AND hour between 10 AND 11) -- Get the name of the persons that have been in the bakery from 10am to 11am. Should cross with passengers list?

-- idea: cross flights on 7 after 10 with list above


SELECT transcript FROM interviews WHERE year =2021 AND month = 7 AND day = 28 -- Check interviews trancript. Note: thief left on car after 10 min of the thef. Thief withdraw money in that morning on Laggett Street. Witness heard call where thief plan to catch a flight the next morning and ask someone to purchase the ticket. Call duration < 1min

SELECT DISTINCT atm_location FROM atm_transactions -- check atm locations (checking speling errors. Legget, not Lagget)

--Conditions to aplly in code to find the Thief:
--List of persons that have been in the bakery that morning, leaved by car between 10:15 and 10:25,
--withdraw money that morning at Leggett Street, flow in the earliest flight in the next day, and made a call on 28 of less than 1 min


SELECT DISTINCT people.name FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
JOIN flights ON passengers.flight_id = flights.id
JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
JOIN phone_calls ON phone_calls.caller = people.phone_number WHERE people.license_plate IN
(SELECT license_plate FROM bakery_security_logs WHERE month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <=25 and activity = 'exit')
AND passengers.flight_id = (SELECT id FROM flights WHERE flights.year = 2021 AND flights.month = 7 AND flights.day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville' ) ORDER by hour, minute LIMIT 1)
AND atm_transactions.month = 7 AND atm_transactions.day = 28 AND atm_transactions.atm_location = 'Leggett Street' AND atm_transactions.transaction_type = 'withdraw'
AND phone_calls.year = 2021 AND phone_calls.month= 7 AND phone_calls.day = 28 AND phone_calls.duration < 60

Finding destination

SELECT city FROM airports WHERE id = (SELECT destination_airport_id FROM flights WHERE
year = 2021 AND month = 7 AND day = 29 AND origin_airport_id = (
SELECT id FROM airports WHERE city = 'Fiftyville') ORDER BY hour, minute LIMIT 1)

Finding accomplice using phone calls

SELECT phone_number FROM people WHERE name = 'Bruce' -- getting bruce number. Admiting there is only one BRUCE. (367) 555-5533


SELECT name FROM people WHERE phone_number =
(SELECT receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60 AND caller = '(367) 555-5533') -- using known call made on the robery day and Bruce phone to find accomplice
