import React from 'react';
import {createRoot} from 'react-dom/client';
import {ChakraProvider, ColorModeScript} from "@chakra-ui/react";
import {RouterProvider} from "react-router";
import router from "./router";
import theme from "./theme";
import {QueryClient, QueryClientProvider} from "@tanstack/react-query";

const client = new QueryClient();


const root = createRoot(
    document.getElementById('root') as HTMLElement
);
root.render(
    <QueryClientProvider client={client}>
        <ChakraProvider theme={theme}>
            <ColorModeScript initialColorMode={theme.config.initialColorMode}/>

            <RouterProvider router={router}/>
        </ChakraProvider>
    </QueryClientProvider>
);
