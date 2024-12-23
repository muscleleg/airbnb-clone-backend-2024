import {Outlet} from "react-router";
import {
    Box,
} from "@chakra-ui/react";
import React from "react";
import Header from "./Header";



export default function Root() {
    return <Box>
        <Header/>

        <Outlet/>

    </Box>
}