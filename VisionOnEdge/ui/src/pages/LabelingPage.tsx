import React, { FC, useEffect, useRef } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Flex, Button, Text } from '@fluentui/react-northstar';

import Scene from '../components/LabelingPage/Scene';
import { LabelingType, Annotation } from '../store/labelingPage/labelingPageTypes';
import { State } from '../store/State';
import { LabelImage } from '../store/part/partTypes';
import { saveAnnotation, getAnnotations } from '../store/labelingPage/labelingPageActions';

interface LabelingPageProps {
  labelingType: LabelingType;
  imageIndex: number;
  closeDialog: () => void;
}
const LabelingPage: FC<LabelingPageProps> = ({ labelingType, imageIndex, closeDialog }) => {
  const { images, annotations } = useSelector<State, { images: LabelImage[]; annotations: Annotation[] }>(
    (state) => ({
      images: state.part.capturedImages,
      annotations: state.labelingPageState.annotations,
    }),
  );
  const imageUrl = images[imageIndex].image;
  const imageId = images[imageIndex].id;
  const dispatch = useDispatch();
  const exist = useRef<boolean>(false);

  useEffect(() => {
    exist.current = false;
    dispatch(getAnnotations(imageId));
  }, [dispatch, imageId]);

  useEffect(() => {
    if (annotations.length > 0) {
      exist.current = true;
    }
  }, [annotations]);

  return (
    <Flex column hAlign="center">
      <Text size="larger" weight="semibold">
        DRAW A RECTANGLE AROUND THE PART
      </Text>
      <Scene url={imageUrl} labelingType={labelingType} />
      <Flex gap="gap.medium">
        <Flex gap="gap.medium">
          <Button
            primary
            content="Save"
            onClick={(): void => {
              dispatch(saveAnnotation(images[imageIndex], annotations, exist.current));
              closeDialog();
            }}
          />
          <Button
            content="Cancel"
            onClick={(): void => {
              closeDialog();
            }}
          />
        </Flex>
      </Flex>
    </Flex>
  );
};

export default LabelingPage;
