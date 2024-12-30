import {Box, Button, Grid, Heading, HStack, Image, Text, useColorModeValue, VStack} from "@chakra-ui/react";
import {FaRegHeart, FaStar} from "react-icons/fa";

interface IRoomProps {
    imageUrl: string;
    name: string;
    rating: number;
    city: string;
    country: string;
    price: number;
}


export default function Room({imageUrl, name, rating, city, country, price}: IRoomProps) {
    const gray = useColorModeValue("gray.600", "gray.300");
    return (
        <VStack alignItems={"flex-start"}>
            <Box position="relative" overflow="hidden" rounded="3xl" mb={2}>
                    <Image
                        w="230px"
                        h="280px"
                        objectFit="cover"
                        src={imageUrl}
                    />
                <Button variant={"unstyled"} position="absolute" top={0} right={0} color="white">
                    <FaRegHeart size="25px"/>
                </Button>
            </Box>
            <Box alignItems={"flex-start"} pl={"5px"}>
                <Grid gap={2} alignItems="center" templateColumns={"6fr 1fr"}>
                    <Heading noOfLines={1} fontSize="sm">
                        {name}
                    </Heading>
                    <HStack _hover={{color: "red.100"}} spacing={1}>
                        <FaStar size={12}/>
                        <Text>{rating}</Text>
                    </HStack>
                </Grid>
                <Text fontSize={"sm"} color={gray}>{city},{country}</Text>
                <Box><Text as="b">{price}</Text> / night</Box>
            </Box>
        </VStack>
    );
}