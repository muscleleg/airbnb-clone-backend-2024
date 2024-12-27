import {Box, Button, Grid, Heading, HStack, Image, Skeleton, SkeletonText, Text, VStack} from "@chakra-ui/react";
import {FaHeart, FaRegHeart, FaStar} from "react-icons/fa";
import Room from "../components/Room";

export default function Home() {
    return <Grid mt={10}
                 px={{
                     base: 10, lg: 40,
                 }}
                 columnGap={4}
                 rowGap={8}
                 templateColumns={{
                     sm: "1fr",
                     md: "1fr 1fr",
                     lg: "repeat(3,1fr)",
                     xl: "repeat(4,1fr)",
                     "2xl": "repeat(5,1fr)",
                 }}>
        <Box display="flex" flexDirection={"column"} justifyContent={"space-between"}>
            <Skeleton height={280} rounded="3xl" mb={2}/>
            <Box display="flex" pt={2} minH={69}>
                <SkeletonText noOfLines={3} w="50%" />
            </Box>
        </Box>
        <Room/>


    </Grid>
}