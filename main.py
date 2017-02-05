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
        error = self.request.get("error")
        error_element = error if error else ""

        error2 = self.request.get("error2")
        error_element2 = error2 if error2 else ""

        error3 = self.request.get("error3")
        error_element3 = error3 if error3 else ""

        error4 = self.request.get("error4")
        error_element4 = error4 if error4 else ""

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
        content = page_header + edit_header + forms.format(error_element,error_element2,error_element3,error_element4,username,password,verify,email) + page_footer 
        self.response.write(content)

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')
        error = "Invalid Username"
        error2 = "Invalid Password"
        error3 = "Your passwords did not match!"
        error4 = "Invalid Email"

        if not self.valid_username(username) and not self.valid_password(password) and not self.valid_email(email) and password != verify:
            self.redirect("/?error=" + error + "&error2=" + error2 +"&error3="+error3+"&error4="+error4+ "&username=" +username +"&email="+ email +"&password=" + password + "&verify="+verify) 
        elif not self.valid_username(username) and not self.valid_password(password) and not self.valid_email(email):
            self.redirect("/?error=" + error + "&error2=" + error2 +"&error4="+error4+ "&username=" +username +"&email="+ email +"&password=" + password + "&verify="+verify)  
        elif password != verify and not self.valid_username(username):
            self.redirect("/?error3=" + error3 + "&error=" + error + "&username=" +username +"&email="+ email +"&password=" + password + "&verify="+verify)
        elif password != verify and not self.valid_password(password):
            self.redirect("/?error2=" + error2 + "&error3=" + error3 +"&username=" +username +"&email="+ email +"&password=" + password + "&verify="+verify)
        elif password != verify and not self.valid_email(email):
            self.redirect("/?error3=" + error3 + "&error4=" + error4+"&username=" +username +"&email="+ email +"&password=" + password + "&verify="+verify) 
        elif password != verify:
            self.redirect("/?error3=" + error3 +"&username=" +username +"&email="+ email +"&password=" + password + "&verify="+verify)
        elif not self.valid_username(username):
            self.redirect("/?error=" + error + "&username=" +username +"&email="+ email +"&password=" + password + "&verify="+verify)
        elif not self.valid_password(password) and not self.valid_email(email):
            self.redirect("/?error2=" + error2 +"&error4="+error4+ "&username=" +username +"&email="+ email +"&password=" + password + "&verify="+verify) 
        elif not self.valid_email(email):
            self.redirect("/?error4=" + error4+"&username=" +username +"&email="+ email +"&password=" + password + "&verify="+verify)
        else:
            # build response content
            sentence = "<h2> Welcome, " + username + "!</h2>"
            content = page_header + "<p>" + sentence + "</p>" + page_footer
            self.response.write(content)
                
app = webapp2.WSGIApplication([
    ('/', Main)
], debug=True)