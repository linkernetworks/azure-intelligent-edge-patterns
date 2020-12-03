/* eslint-disable react/display-name */

import React from 'react';
import { Pivot, PivotItem } from '@fluentui/react';

import { MainImagesProps } from './ts';

import { FilteredImgList } from './FilteredImgList';
import { UntaggedPivot } from './UntaggedPivot';
import { Instruction } from '../Instruction';
import { EmptyAddIcon } from '../EmptyAddIcon';

export const MainImages: React.FC<MainImagesProps> = ({
  labeledImages,
  unlabeledImages,
  relabelImages,
  filteredCameras,
  filteredParts,
  imageAddedButNoAnno,
  labeledImagesLessThanFifteen,
  onUpload,
  openCaptureDialog,
}) => {
  const onRenderInstructionInsidePivot = () => (
    <>
      {imageAddedButNoAnno && (
        <Instruction
          title="Successfully added images!"
          subtitle="Now identify what is in your images to start training your model."
          smallIcon
        />
      )}
      {labeledImagesLessThanFifteen && (
        <Instruction
          title="Images have been tagged!"
          subtitle="Continue adding and tagging more images to improve your model. We recommend at least 15 images per object."
          smallIcon
        />
      )}
    </>
  );

  if (labeledImages.length + unlabeledImages.length)
    return (
      <Pivot>
        <PivotItem headerText="Untagged">
          {onRenderInstructionInsidePivot()}
          <UntaggedPivot
            unlabeledImages={unlabeledImages}
            relabelImages={relabelImages}
            filteredCameras={filteredCameras}
            filteredParts={filteredParts}
            openCaptureDialog={openCaptureDialog}
            onUpload={onUpload}
          />
        </PivotItem>
        <PivotItem headerText="Tagged">
          {onRenderInstructionInsidePivot()}
          <FilteredImgList
            images={labeledImages}
            filteredCameras={filteredCameras}
            filteredParts={filteredParts}
          />
        </PivotItem>
      </Pivot>
    );

  return (
    <EmptyAddIcon
      title="Add images"
      subTitle="Capture images from your video streams and tag parts"
      primary={{ text: 'Capture from camera', onClick: openCaptureDialog }}
      secondary={{ text: 'Upload images', onClick: onUpload }}
    />
  );
};
