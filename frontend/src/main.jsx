import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'

import { StytchProvider } from '@stytch/react';
import { createStytchUIClient } from '@stytch/react/ui';

const stytch = createStytchUIClient('public-token-test-a4437b81-c48e-43f0-8adf-bd5ea8b777c9');


import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
      <StytchProvider stytch={stytch}>
        <App />
      </StytchProvider>
  </StrictMode>,
)
