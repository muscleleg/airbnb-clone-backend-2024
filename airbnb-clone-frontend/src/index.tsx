import React from 'react';
import { createRoot } from 'react-dom/client';
import {ChakraProvider} from "@chakra-ui/react";
import {RouterProvider} from "react-router";
import router from "./router";

const root = createRoot(
    document.getElementById('root') as HTMLElement
);
root.render(
    <React.StrictMode>
        <ChakraProvider>
            <RouterProvider router={router}/>
        </ChakraProvider>
    </React.StrictMode>
);
