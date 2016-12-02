# kobo_selenium_tests

This test suite is written for use on dkobo, kobocat, and Enketo Legacy. **For manual testing steps that include KPI, please see ["Manual Testing of dkobo, kobocat, and KPI"](#manual-testing-of-dkobo-kobocat-and-kpi) below. **

The default test covers the following steps: 

1. Login with an existing account
1. Create a new form from scratch, add a sample question
1. Preview the form
1. Save and close the form
1. Export form to XLS
1. Delete form 
1. Import XLS form
1. Deploy the imported form
1. Open the form in Enketo, enter and submit  data
1. Export data to XLS
1. Delete the project 
1. Log out

## Manual Testing of dkobo, kobocat, and KPI

KPI and dkobo are both form builders, and each user account may only use one at a time. To test both, follow the procedure below to toggle the test user's form builder preference.

1. Begin by logging in as usual;
1. Switch your test user (who's now logged in) to dkobo by going to `https://[YOUR KPI URL]/hub/switch_builder?beta=0`
  1. For most setups, this is `https://[YOUR DOMAIN]/forms/hub/switch_builder?beta=0`
1. Perform steps 2 through 11 (do not log out) in the section above;
1. Switch your test user to KPI by going to `https://[YOUR KPI URL]/hub/switch_builder?beta=1`
  1. For most setups, this is `https://[YOUR DOMAIN]/forms/hub/switch_builder?beta=1`
1. Perform steps 2 through 12 (logging out this time) in the section above.
