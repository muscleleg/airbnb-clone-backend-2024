import React from 'react';
import { createRoot } from 'react-dom/client';
import {ChakraProvider, ColorModeScript} from "@chakra-ui/react";
import {RouterProvider} from "react-router";
import router from "./router";
import theme from "./theme";

const root = createRoot(
    document.getElementById('root') as HTMLElement
);
root.render(
    <React.StrictMode>
        <ChakraProvider theme={theme}>
            <ColorModeScript initialColorMode={theme.config.initialColorMode}/>

            <RouterProvider router={router}/>
        </ChakraProvider>
    </React.StrictMode>
);
