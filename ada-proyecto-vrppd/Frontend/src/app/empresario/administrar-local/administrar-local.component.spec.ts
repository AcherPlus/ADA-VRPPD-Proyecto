import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdministrarLocalComponent } from './administrar-local.component';

describe('AdministrarLocalComponent', () => {
  let component: AdministrarLocalComponent;
  let fixture: ComponentFixture<AdministrarLocalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AdministrarLocalComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AdministrarLocalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
