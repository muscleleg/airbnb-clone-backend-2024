import {useParams} from "react-router";
import {useQuery} from "@tanstack/react-query";
import {getRoom} from "../api";
import {IRoomDetail} from "../types";
import {Box, Grid, GridItem, Heading, Image, Skeleton} from "@chakra-ui/react";
import React from "react";

export default function RoomDetail() {

    const {roomPk} = useParams();
    const {isLoading, data} = useQuery<IRoomDetail>({
        queryKey: [`rooms`, roomPk],
        queryFn: getRoom,
    })
    return (
        <Box
            mt={10}
            px={{
                base: 10,
                lg: 40,
            }}
        >
            <Skeleton height={"43px"} isLoaded={!isLoading} width="50%">
                <Heading>
                    {data?.name}
                </Heading>
            </Skeleton>
            <Grid
                mt={8}
                overflow={"hidden"}
                rounded="lg"
                gap={3}
                height="60vh"
                templateRows={"1fr 1fr"}
                templateColumns={"repeat(4,1fr)"}
            >
                {/* Rounded Corners와 함께 사용할 때
rounded="lg"를 사용하면 Grid 컨테이너의 모서리가 둥글게 렌더링됩니다. 하지만 자식 요소가 부모의 영역을 초과하면 둥근 모서리 밖으로 콘텐츠가 삐져나오는 현상이 발생할 수 있습니다.
overflow: hidden은 이 문제를 방지하고 모서리 안쪽으로 콘텐츠를 잘라줍니다.*/}
                {
                    [0, 1, 2, 3, 4,].map(
                        (photo, index) => (
                            <GridItem
                                colSpan={index === 0 ? 2 : 1}
                                rowSpan={index === 0 ? 2 : 1}
                                overflow={"hidden"}
                                key={index}>
                                <Skeleton isLoaded={!isLoading} h="100%" w="100%">
                                    <Image w="100%" h="100%" objectFit={"cover"} src={data?.photos[index].file}/>
                                </Skeleton>
                            </GridItem>)
                    )
                }
            </Grid>
        </Box>
    );
}