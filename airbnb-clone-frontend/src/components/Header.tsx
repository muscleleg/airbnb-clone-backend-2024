import {Box, Button, HStack, IconButton, useDisclosure} from "@chakra-ui/react";
import {FaAirbnb, FaMoon} from "react-icons/fa";
import LoginModal from "./LoginModal";
import React from "react";
import SignUpModal from "./SingUpModal";

export default function Header() {
    const {isOpen:isLoginOpen, onClose:onLoginClose, onOpen:onLoginOpen} = useDisclosure();
    const {isOpen:isSignUpOpen, onClose:onSignUpClose, onOpen:onSignUpOpen} = useDisclosure();
    return (
        <HStack justifyContent={"space-between"} py={5} px={10} borderBottomWidth={1}>
            <Box color="red.500">
                {/*FaAirbnb는 차크라 ui 요소가 아니라서 red.500으로 color를 줄 수 없음, 찐 색상코드 넣어야함, 그래서 box로 wrapping하는 것임*/}
                <FaAirbnb size={48}/>
            </Box>
            <HStack spacing={2}>
                <IconButton variant={"ghost"} aria-label="Toggle dark mode" icon={<FaMoon/>}/>
                <Button onClick={onLoginOpen}>Log in</Button>
                <Button onClick={onSignUpOpen} colorScheme={"red"}>Sign up</Button>
            </HStack>
            <LoginModal isOpen={isLoginOpen} onClose={onLoginClose}/>
            <SignUpModal isOpen={isSignUpOpen} onClose={onSignUpClose}/>
        </HStack>
    );
}