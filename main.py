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

        # if we have an error
        error = self.request.get("error")
        error_element = error if error else ""

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
                            <label class = "error">
                                <input type="text" name="username"/> {0}
                            </label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label>
                                Password     
                            </label>
                            <label class = "error">
                                <input type="text" name="password"/> {1}
                            </label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label>
                                Verify Password
                            </label>
                            <label class = "error">
                                <input type="text" name="verify"/> {2}
                            </label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label>
                                Email(optional)     
                            </label>
                            <label class = "error">
                                <input type="text" name="email"/> {3}
                            </label>
                        </td>
                    </tr>
                </tbody>
            </table>
            <input type ="Submit">
        </form>
        """
           
        
        

        # combine all the pieces to build the content of our response 
        if error_element == "Invalid Username":
            content = page_header + edit_header + forms.format(error_element,"","","") + page_footer 
            self.response.write(content)
        elif error_element == "Invalid Password":
            content = page_header + edit_header + forms.format("",error_element,"","") + page_footer 
            self.response.write(content)
        elif error_element == "Your passwords did not match!":
            content = page_header + edit_header + forms.format("","",error_element,"") + page_footer 
            self.response.write(content)
        elif error_element == "Invalid Email":
            content = page_header + edit_header + forms.format("","","",error_element) + page_footer 
            self.response.write(content)
        else:
            content = page_header + edit_header + forms.format(error_element,error_element,error_element,error_element) + page_footer 
            self.response.write(content)
    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        if not valid_username(username):
            error = "Invalid Username"
            self.redirect("/?error=" + cgi.escape(error, quote=True))
            have_error = True

        elif not valid_password(password):
            error = "Invalid Password"
            self.redirect("/?error=" + cgi.escape(error, quote=True))
            have_error = True
            
        elif password != verify:
            error = "Your passwords did not match!"
            self.redirect("/?error=" + cgi.escape(error, quote=True))
            have_error = True

        elif not valid_email(email):
            error = "Invalid Email"
            self.redirect("/?error=" + cgi.escape(error, quote=True))
            have_error = True

        elif not have_error:
            # build response content
            sentence = " Welcome, " + username + "!"
            content = page_header + "<p>" + sentence + "</p>" + page_footer
            self.response.write(content)
                
app = webapp2.WSGIApplication([
    ('/', Main)
], debug=True)