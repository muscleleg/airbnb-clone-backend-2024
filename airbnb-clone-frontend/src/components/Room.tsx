import {Box, Button, Grid, Heading, HStack, Image, Text, useColorModeValue, VStack} from "@chakra-ui/react";
import {FaRegHeart, FaStar} from "react-icons/fa";

export default function Room() {
    const gray = useColorModeValue("gray.600","gray.300");
    return (
        <VStack>
            <Box position="relative" overflow="hidden" rounded="3xl" mb={2}>
                <Image minH="280" objectFit="cover"
                       src="https://a0.muscache.com/im/pictures/prohost-api/Hosting-771540516262842487/original/2c9354ff-c3ac-471b-a265-3a20b5228528.jpeg?im_w=720&im_format=avif"/>
                <Button variant={"unstyled"} position="absolute" top={0} right={0} color="white">
                    <FaRegHeart size="25px"/>
                </Button>
            </Box>
            <Box alignItems={"flex-start"}>
                <Grid gap={2} alignItems="center" templateColumns={"6fr 1fr"}>
                    <Heading noOfLines={1} fontSize="sm">
                        Cheomdangwahak-ro,Jeongeup-si, North Jeolla Province, South Korea
                    </Heading>
                    <HStack _hover={{color:"red.100"}} spacing={1}>
                        <FaStar size={12}/>
                        <Text>5.0</Text>
                    </HStack>
                </Grid>
                <Text fontSize={"sm"} color={gray}>Seoul, S. Korea</Text>
                <Box><Text as="b">$72</Text> / night</Box>
            </Box>
        </VStack>
    );
}