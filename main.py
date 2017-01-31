import webapp2
import cgi
import re 

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
  
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)

class Main(webapp2.RequestHandler):
    def get(self):
        
        edit_header = "<h3>Signup</h3>"

       #a form for entering the username/password/email
        forms = """
        <form action = "/" method = "post">
            <table>
                <tbody>
                    <tr>
                        <td>
                            <label>
                                Username     
                            </label>
                            <label>
                                <input type="text" name="username"/>
                            </label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label>
                                Password     
                            </label>
                            <label>
                                <input type="text" name="password"/>
                            </label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label>
                                Verify Password
                            </label>
                            <label>
                                <input type="text" name="verify"/>
                            </label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label>
                                Email(optional)     
                            </label>
                            <label>
                                <input type="text" name="email"/>
                            </label>
                        </td>
                    </tr>
                </tbody>
            </table>
            <input type ="Submit">
        </form>
        """

        # if we have an error, make a <p> to display it
        error = self.request.get("error")
        error_element = "<p class='error'>" + error + "</p>" if error else ""

        # combine all the pieces to build the content of our response 
        content = page_header + edit_header + forms + page_footer + error_element
        self.response.write(content)

    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        params = dict(username = username,
                      email = email)

        if not valid_username(username):
            error = "Invalid Username"
            self.redirect("/?error=" + cgi.escape(error, quote=True))
            have_error = True

        if not valid_password(password):
            error = "Invalid Password"
            self.redirect("/?error=" + cgi.escape(error, quote=True))
            have_error = True
        elif password != verify:
            error = "Your passwords did not match!"
            self.redirect("/?error=" + cgi.escape(error, quote=True))
            have_error = True

        if not valid_email(email):
            error = "Invalid Email"
            self.redirect("/?error=" + cgi.escape(error, quote=True))
            have_error = True

        if not have_error:
            # build response content
            sentence = " Welcome, " + username + "!"
            content = page_header + "<p>" + sentence + "</p>" + page_footer
            self.response.write(content)
                
app = webapp2.WSGIApplication([
    ('/', Main)
], debug=True)