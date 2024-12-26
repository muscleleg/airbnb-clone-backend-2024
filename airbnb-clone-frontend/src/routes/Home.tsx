import {Box, Grid, Heading, HStack, Image, Text, VStack} from "@chakra-ui/react";
import {FaStar} from "react-icons/fa";

export default function Home() {
    return <Grid mt={10} px={40} columnGap={4} rowGap={8} templateColumns={"repeat(5,1fr)"}>
        <VStack alignItems={"flex-start"}>
            <Box overflow="hidden" rounded="3xl" mb={2}>
                <Image h="280"  objectFit="cover"
                       src="https://a0.muscache.com/im/pictures/prohost-api/Hosting-771540516262842487/original/2c9354ff-c3ac-471b-a265-3a20b5228528.jpeg?im_w=720&im_format=avif"/>
            </Box>
            <Grid gap={2} templateColumns={"3fr 1fr"}>
                <Heading noOfLines={1} fontSize="md">
                    Cheomdangwahak-ro,Jeongeup-si, North Jeolla Province, South Korea
                </Heading>
                <HStack spacing={1}>
                    <FaStar size={15}/>
                    <Text>5.0</Text>
                </HStack>
            </Grid>
            <Text fontSize={"sm"} color="gray.400">Seoul, S. Korea</Text>
            <Text as="b">$72</Text> / night
        </VStack>


    </Grid>
}