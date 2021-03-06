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

class Main(webapp2.RequestHandler):

    def valid_username(self, username):
        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        if USER_RE.match(username):
            return username
        else: 
            return "" 

    def valid_password(self, password):
        PASS_RE = re.compile(r"^.{3,20}$")
        if PASS_RE.match(password):
            return password
        else:
            return ""

    def valid_email(self, email):
        EMAIL_RE  = re.compile(r'^[\S]*@[\S]*\.[\S]*$')
        if EMAIL_RE.match(email):
            return email
        else:
            return ""

    def get(self):
        
        edit_header = "<h1>Signup</h1>"

        # if we have an error
        error_username = self.request.get("error_username")
        error_element_username = error_username if error_username else ""

        error_password = self.request.get("error_password")
        error_element_password = error_password if error_password else ""

        error_verify = self.request.get("error_verify")
        error_element_verify = error_verify if error_verify else ""

        error_email = self.request.get("error_email")
        error_element_email = error_email if error_email else ""

        username = self.request.get("username")
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')


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
                                <input type="text" name="username" value = "{4}" / > {0} 
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
                            <label class = "error">
                                <input type="text" name="password" value = "{5}"/> {1}
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
                            <label class = "error">
                                <input type="text" name="verify" value = "{6}" /> {2}
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
                            <label class = "error">
                                <input type="text" name="email" value = "{7}"/> {3}
                            </label>
                        </td>
                    </tr>
                </tbody>
            </table>
            <input type ="Submit">
        </form>
        """
        content = page_header + edit_header + forms.format(error_element_username,error_element_password,error_element_verify,error_element_email,username,password,verify,email) + page_footer 
        self.response.write(content)

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')
        error_username = "Invalid Username"
        error_password = "Invalid Password"
        error_verify = "Your passwords did not match!"
        error_email = "Invalid Email"

        error_url = "/?"

        if not self.valid_username(username):
            error_url += "&error_username=" +error_username+"&username="+username+"&email=" +email+"&verify=" +verify+ "&password=" +password
        
        if email == "":
            email = ""
        elif not self.valid_email(email):
            error_url += "&error_email=" +error_email+ "&username="+username+"&email=" +email+"&verify=" +verify+ "&password=" +password
        
        if not self.valid_password(password):
            error_url += "&error_password=" +error_password+ "&username="+username+"&email=" +email+"&verify=" +verify+ "&password=" +password

        if password != verify:
            error_url += "&error_verify=" +error_verify+ "&username="+username+"&email=" +email+"&verify=" +verify+ "&password=" +password
                
        if not error_url == "/?":
            self.redirect(error_url)
        else:
            # build response content
            sentence = "<h2> Welcome, " + username + "!</h2>"
            content = page_header + "<p>" + sentence + "</p>" + page_footer
            self.response.write(content)
                
app = webapp2.WSGIApplication([
    ('/', Main)
], debug=True)