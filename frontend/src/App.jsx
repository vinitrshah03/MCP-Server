import './App.css'
import {StytchLogin, IdentityProvider, useStytchUser} from '@stytch/react';

function App() {
  const {user} = useStytchUser();

  const config = {
        "products": [
          "oauth",
          "passwords",
          "otp"
        ],
        "oauthOptions": {
          "providers": [
            {
              "type": "google"
            }
          ],
          "loginRedirectURL": "https://www.stytch.com/login",
          "signupRedirectURL": "https://www.stytch.com/signup"
        },
        "otpOptions": {
          "methods": [
            "sms",
            "whatsapp"
          ],
          "expirationMinutes": 5
        },
        "passwordOptions": {
          "loginRedirectURL": "https://www.stytch.com/login",
          "resetPasswordRedirectURL": "https://www.stytch.com/reset-password"
        }
}
  return (
    <div>
      {!user ? <StytchLogin config={config}/> : <IdentityProvider />}
    </div>
  )
}

export default App
