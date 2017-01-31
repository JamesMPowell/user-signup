import webapp2
import cgi

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
        form
        {
            display: block;
            margin-top: 0em;
        }
        tr{
            display: table-row;
        }
        table
        {
            display: table;
            border-collapse: seperate;
            border-spacing: 2px;
            border-color: grey;
        }
        tbody
        {
            display:table-row-group;
            vertical-align:middle;
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
    def get(self):
        
        edit_header = "<h3>Signup</h3>"




       #a form for entering the username/password/email
        forms = """
        <form method = "post">
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
        </form>
        """
        submit = """
            <input type= "submit" value = "Submit">
        """

        # if we have an error, make a <p> to display it
        error = self.request.get("error")
        error_element = "<p class='error'>" + error + "</p>" if error else ""
		
		#example of alternate if statement
		#error_element = ""
		#if error:
		#	error_element = "<p class='error'>" + error + "</p>"

		
        # combine all the pieces to build the content of our response
        main_content = edit_header + forms + submit + error_element
        content = page_header + main_content + page_footer
        self.response.write(content)
        
class username(webapp2.RequestHandler):
    def post(self):
       
        # look inside the request to figure out what the user typed
        username = self.request.get("username")

         # if the user typed nothing at all, redirect and yell at them
        if(not username) or (username.strip() == ""):
            error = "Please specify the movie you want to add."
            self.redirect("/?error=" + cgi.escape(error, quote=True))
#class password(webapp2.RequestHandler):
#    def post(self):
        # to do password entry/verification

#class email(webapp2.RequestHandler):
#    def post(self):
        #to do email entry/verification

        
app = webapp2.WSGIApplication([
    ('/', Main)
], debug=True)