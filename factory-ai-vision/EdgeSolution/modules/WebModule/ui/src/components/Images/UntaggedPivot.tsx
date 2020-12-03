import React from 'react';
import { MessageBar, Separator, mergeStyleSets } from '@fluentui/react';

import { UntaggedPivotProps } from './ts';

import { FilteredImgList } from './FilteredImgList';
import { EmptyAddIcon } from '../EmptyAddIcon';

const classes = mergeStyleSets({
  seperator: {
    margin: '20px 0px',
  },
});

export const UntaggedPivot: React.FC<UntaggedPivotProps> = ({
  relabelImages,
  unlabeledImages,
  filteredCameras,
  filteredParts,
  openCaptureDialog,
  onUpload,
}) => {
  if (
    unlabeledImages.length === 0
    && relabelImages.length === 0
  )
    return (
      <EmptyAddIcon
        title="Looks like you don’t have any untagged images"
        subTitle="Continue adding and tagging more images from your video streams to improve your model"
        primary={{ text: 'Capture from camera', onClick: openCaptureDialog }}
        secondary={{ text: 'Upload images', onClick: onUpload }}
      />
    );

  return (
    <>
      {
        relabelImages.length > 0
        && (
          <>
            <Separator alignContent="start" className={classes.seperator}>
              Deployment captures
            </Separator>
            <MessageBar styles={{ root: { margin: '12px 0px' } }}>
              Images saved from the current deployment. Confirm or modify the objects identified to improve your
              model.
            </MessageBar>
            <FilteredImgList
              images={relabelImages}
              filteredCameras={filteredCameras}
              filteredParts={filteredParts}
            />
          </>
        )
      }
      {
        unlabeledImages.length > 0
        && (
          <>
            <Separator alignContent="start" className={classes.seperator}>
              Manually added
            </Separator>
            <FilteredImgList
              images={unlabeledImages}
              filteredCameras={filteredCameras}
              filteredParts={filteredParts}
            />
          </>
        )
      }
    </>
  );
};
