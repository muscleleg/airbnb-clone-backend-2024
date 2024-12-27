import {
    Box,
    Button,
    HStack,
    IconButton,
    LightMode, Stack,
    useColorMode,
    useColorModeValue,
    useDisclosure
} from "@chakra-ui/react";
import {FaAirbnb, FaMoon, FaSun} from "react-icons/fa";
import LoginModal from "./LoginModal";
import React from "react";
import SignUpModal from "./SingUpModal";

export default function Header() {
    const {isOpen: isLoginOpen, onClose: onLoginClose, onOpen: onLoginOpen} = useDisclosure();
    const {isOpen: isSignUpOpen, onClose: onSignUpClose, onOpen: onSignUpOpen} = useDisclosure();
    const {toggleColorMode} = useColorMode();
    const logColor = useColorModeValue("red.500", "red.200");
    const Icon = useColorModeValue(FaMoon, FaSun)
    return (
        <Stack justifyContent={"space-between"}
               alignItems="center"
               py={5}
               px={40}
               borderBottomWidth={1}
               direction={{sm: "column", md: 'row'}}
               spacing={{sm:3,md:0}}
        >
            <Box color={logColor}>
                {/*FaAirbnb는 차크라 ui 요소가 아니라서 red.500으로 color를 줄 수 없음, 찐 색상코드 넣어야함, 그래서 box로 wrapping하는 것임*/}
                <FaAirbnb size={48}/>
            </Box>
            <HStack spacing={2}>
                <IconButton
                    onClick={toggleColorMode}
                    variant={"ghost"} aria-label="Toggle dark mode"
                    icon={<Icon/>}/>
                <Button onClick={onLoginOpen}>Log in</Button>
                <LightMode>
                    <Button onClick={onSignUpOpen} colorScheme={"red"}>Sign up</Button>
                </LightMode>
            </HStack>
            <LoginModal isOpen={isLoginOpen} onClose={onLoginClose}/>
            <SignUpModal isOpen={isSignUpOpen} onClose={onSignUpClose}/>
        </Stack>
    );
}