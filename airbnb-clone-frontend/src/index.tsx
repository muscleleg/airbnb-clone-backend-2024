import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';
import {ChakraProvider} from "@chakra-ui/react";
import { defaultSystem } from "@chakra-ui/react"

const root = createRoot(
    document.getElementById('root') as HTMLElement
);
root.render(
    <React.StrictMode>
        <ChakraProvider value={defaultSystem}>
            <App/>
        </ChakraProvider>
    </React.StrictMode>
);
