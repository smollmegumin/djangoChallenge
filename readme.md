# Django challenge by Eduardo Avila 🎊

# Register user:
`curl --location --request POST 'https://djangotestinterview.herokuapp.com/auth/' \
--form 'username=test2' \
--form 'password=password' \
--form 'email=test@test.com'`

---
# Login
`curl --location --request POST 'https://djangotestinterview.herokuapp.com/access/' \
--form 'username=test2' \
--form 'password=password'`

---
# Get cars
`curl --location --request GET 'https://djangotestinterview.herokuapp.com/api/cars/' \
--header 'Authorization: Token YOUR_TOKEN_HERE' \
--form 'username=zz' \
--form 'newPlacas=zzz'`

---
# Add Car
`curl --location --request POST 'https://djangotestinterview.herokuapp.com/api/cars/' \
--header 'Authorization: Token YOUR_TOKEN_HERE' \
--form 'lat=10' \
--form 'placas=ss' \
--form 'lon=10'`

---

# Delete car
`curl --location --request DELETE 'https://djangotestinterview.herokuapp.com/api/cars/' \
--header 'Authorization: Token YOUR_TOKEN_HERE' \
--form 'placas=ss'`

---

# Update car
`curl --location --request PATCH 'https://djangotestinterview.herokuapp.com/api/cars/' \
--header 'Authorization: Token YOUR_TOKEN_HERE' \
--form 'newPlacas=10' \
--form 'placas=ss'`