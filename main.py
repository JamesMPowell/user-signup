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
        .error2 {
            color: red;
        }
        .error3 {
            color: red;
        }
        .error4{
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
        
        edit_header = "<h1>Signup</h1>"

        # if we have an error
        error = self.request.get("error")
        error_element = error if error else ""

        error2 = self.request.get("error2")
        error_element2 = error2 if error2 else ""

        error3 = self.request.get("error3")
        error_element3 = error3 if error3 else ""

        error4 = self.request.get("error4")
        error_element4 = error4 if error4 else ""


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
                        </td>
                        <td>
                            <label class = "error">
                                <input type="text" name="username" value = ""/ >{0} 
                            </label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label>
                                Password     
                            </label>
                        </td>
                        <td>
                            <label class = "error2">
                                <input type="text" name="password" value = ""/> {1}
                            </label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label>
                                Verify Password
                            </label>
                        </td>
                        <td>
                            <label class = "error3">
                                <input type="text" name="verify" value = ""/> {2}
                            </label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label>
                                Email(optional)     
                            </label>
                        </td>
                        <td>
                            <label class = "error4">
                                <input type="text" name="email" value = ""/>{3}
                            </label>
                        </td>
                    </tr>
                </tbody>
            </table>
            <input type ="Submit">
        </form>
        """
           
        content = page_header + edit_header + forms.format(error_element,error_element2,error_element3,error_element4) + page_footer 
        self.response.write(content)

    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        if not valid_username(username) :
            error = "Invalid Username"
            self.redirect("/?error=" + cgi.escape(error, quote=True))
            have_error = True

        elif not valid_password(password):
            error2 = "Invalid Password"
            self.redirect("/?error2=" + cgi.escape(error2, quote=True))
            have_error = True
            
        elif password != verify:
            error3 = "Your passwords did not match!"
            self.redirect("/?error3=" + cgi.escape(error3, quote=True))
            have_error = True

        elif not valid_email(email):
            error4 = "Invalid Email"
            self.redirect("/?error4=" + cgi.escape(error4, quote=True))
            have_error = True

        elif not have_error:
            # build response content
            sentence = "<h2> Welcome, " + username + "!</h2>"
            content = page_header + "<p>" + sentence + "</p>" + page_footer
            self.response.write(content)
                
app = webapp2.WSGIApplication([
    ('/', Main)
], debug=True)